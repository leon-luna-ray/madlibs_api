<template>
  <main>
    <h1>Madlibs Chatbot</h1>
    <p>Ask the chatbot to write a Madlibs story for you!</p>
    <p>Response:</p>
    <p>{{ response }}</p>
  </main>
</template>

<script setup>
import { ref, onMounted, computed } from "vue";

const MISTRAL_API_BASE = import.meta.env.VITE_MISTRAL_API_BASE;
const MISTRAL_API_KEY = import.meta.env.VITE_MISTRAL_API_KEY;

const data = ref(null);

const response = computed(()=>{
  if(data.value){
    return data.value.choices[0]?.message?.content;
  }
  return null;
})

const fetchChatResponse = async () => {
  const endpoint = `${MISTRAL_API_BASE}/chat/completions`;
  console.log("API Endpoint:", endpoint);

  const model = "codestral-mamba-latest";
  const messages = [
    {
      role: "user",
      content: "Write a Madlibs story and return it as an array of objects",
    },
  ];

  const payload = {
    model,
    messages,
  };

  try {
    const response = await fetch(endpoint, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${MISTRAL_API_KEY}`,
      },
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      console.error(`HTTP error! status: ${response.status}`);
      const errorText = await response.text();
      console.error("Error response:", errorText);
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    data.value = await response.json();
    console.log("Response data:", data);
  } catch (error) {
    console.error("Error fetching chat response:", error);
  }
}

onMounted(() => {
  fetchChatResponse();
});
</script>
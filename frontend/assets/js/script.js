$(document).ready(function renderPage() {
  const query = `/api/random`;

  $.ajax({
    url: query,
  }).then(function (result) {
    const wordBlanks = result.blanks;
    const storyTitle = result.title;
    const storyText = result.value;

    for (let i = 0; i < wordBlanks.length; i++) {
      const blankIndex = wordBlanks[i];

      $('.word-blanks').append('<input><li>' + blankIndex + '</li><br>');
      $('li').attr('class', 'word-type');
      $('input').attr('class', 'user-input');
    }

    let userWords = [];
    let userStory = [];

    function renderStory() {
      $('.choose-words-page').attr('id', 'hide');
      $('.story-page').attr('id', 'show');

      $('.user-input').each(function () {
        userWords.push($(this).val());
      });

      userStory = storyText.map(function (value, index) {
        return value + userWords[index];
      });

      userStory.toString();

      $('.title').text(storyTitle);
      $('.story-text').text(userStory);
    }

    $('.start-btn').click(renderStory);
  });
});

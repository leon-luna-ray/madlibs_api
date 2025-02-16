import axios from 'axios';

const BASE_API_URL = import.meta.env.VITE_BASE_API_URL || '/api/v1';

axios.defaults.baseURL = BASE_API_URL;

export default axios;
interface Config {
    API_URL: string;
    TIMEOUT: number;
    MAX_RETRIES: number;
    APP_NAME: string;
  }
  
  const config: Config = {
    API_URL: 'http://localhost:8000/api',
    TIMEOUT: 5000,
    MAX_RETRIES: 3,
    APP_NAME: 'mecanica'
  };
  
  export default config;
    
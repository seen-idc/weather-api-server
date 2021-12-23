module.exports = {
    apps : [{
      name   : "weather-api",
      script : "flask run",
      env_production: {
        API_KEY: "api"
      },
      env_development: {
        API_KEY: "api"
      }
    }]
  }
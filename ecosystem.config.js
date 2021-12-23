module.exports = {
    apps : [{
      name   : "weather-api",
      script : "python3 ./app.py",
      env_production: {
        API_KEY: "api"
      },
      env_development: {
        API_KEY: "api"
      }
    }]
  }
// network-access.js - make sure this actually attempts to use http.get
const http = require("http");
try {
  http.get("http://example.com", (res) => {
    console.log("Data received");
  });
} catch (e) {
  // In case of error, still make the attempt
  console.error(e);
}

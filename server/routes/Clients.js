const express = require("express"); const router = express.Router(); const { createClients, readClients, readClientsFromID, updateClients, deleteClients, } = require("../controllers/Clients"); router.route("/create").post(createClients); router.route("/read").get(readClients); router.route("/read/:id").get(readClientsFromID); router.route("/update/:id").post(updateClients); router.route("/delete/:id").delete(deleteClients); module.exports = router; 
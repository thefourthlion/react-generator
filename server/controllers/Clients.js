const Clients = require("../models/Clients");
exports.createClients = async (req, res) => {
  try {
    let newClients = new Clients({
      name: req.body.name,
      phone: req.body.phone,
    });
    await newClients.save();
    res.send(newClients);
  } catch (err) {
    console.log(err);
  }
};
exports.readClients = async (req, res) => {
  const page = req.query.page || 0;
  const limit = req.query.limit || 25;
  try {
    Clients.find({}, (err, result) => {
      if (err) {
        res.json({ app: err });
      }
      res.send(result);
    })
      .sort()
      .skip(page * limit)
      .limit(limit);
  } catch (err) {
    console.log(err);
  }
};
exports.readClientsFromID = async (req, res) => {
  try {
    await Clients.findById({ _id: req.params.id }, {}, (err, result) => {
      if (err) {
        res.json({ app: err });
      }
      res.send(result);
    });
  } catch (err) {
    console.log(err);
  }
};
exports.updateClients = async (req, res) => {
  try {
    await Clients.findByIdAndUpdate(
      req.params.id,
      { name: req.body.name, phone: req.body.phone },
      (err, result) => {
        if (err) {
          res.json({ app: err });
        }
        res.send(result);
      }
    );
  } catch (err) {
    console.log(err);
  }
};
exports.deleteClients = async (req, res) => {
  try {
    if ((await Clients.findById(req.params.id)) === null) {
      res.json({ app: "post not found" });
    } else {
      await Clients.findByIdAndRemove(req.params.id).exec();
      res.json({ app: "post deleted" });
    }
  } catch (err) {
    console.log(err);
    res.send(err);
  }
};

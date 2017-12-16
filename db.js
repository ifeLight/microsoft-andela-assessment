var mongoose = require('mongoose');
mongoose.connect(process.env.DB_URL || "mongodb://mongo:27017/usermanager", { useMongoClient: true });

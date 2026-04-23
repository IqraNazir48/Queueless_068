const mongoose = require('mongoose');

const connectDB = async () => {
    try {
        await mongoose.connect(process.env.MONGO_URI);
        console.log("MongoDB Connected");
    } catch (error) {
        console.error("Database Error:", error.message);
        process.exit(1);
    }
}

module.exports = connectDB;
// adding just a comment to update a file

const client   = require('mongodb').MongoClient;
const employee = require("./employee.js");

let employees = [];
client.connect('mongodb://localhost:27017', function(err, db){
    if(err){
        console.log(err); throw err;
    }
    else{
        console.log("connected" + db);

        let dbo    = db.db       ('employee'); // explicit marking important!!

        let gijun  = employee.make("gijun","o", 24);
        let heejae = employee.make("heejae","seo", 23);

        employee.isExistCollection(dbo, "compressor dept");

        dbo.createCollection("compressor dept", function(err, res){
                    console.log(" [ create the collection ] ");

            if(err) console.log("alread exist");
            else    console.log("create collection");
        });

        employee.store(dbo, "compressor dept", gijun);
        employee.store(dbo, "compressor dept", heejae);

        employee.load(dbo, "compressor dept", employees);

        db.close();
    } // end of if
});

module.exports.run = function(){
    // wait the loadEmployees end
    setTimeout(console.log, 2500, employees);
};

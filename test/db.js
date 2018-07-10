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

        let gijun  = employee.makeEmployee("gijun","o", 24);
        let heejae = employee.makeEmployee("heejae","seo", 23);

        employee.isExistCollection(dbo, "compressor dept");

        dbo.createCollection("compressor dept", function(err, res){
                    console.log(" [ create the collection ] ");

            if(err) console.log("alread exist");
            else    console.log("create collection");
        });

        employee.storeEmployee(dbo, "compressor dept", gijun);
        employee.storeEmployee(dbo, "compressor dept", heejae);

        employee.loadEmployee(dbo, "compressor dept", employees);

        db.close();
    } // end of if
});

module.exports.run = function(){
    // wait the loadEmployees end
    setTimeout(console.log, 2500, employees);
};
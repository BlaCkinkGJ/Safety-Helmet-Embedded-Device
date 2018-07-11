
function Employee(id, firstname, lastname, age){
    this._id = id;
    this.name = firstname + " " + lastname;
    this.firstname = firstname;
    this.lastname = lastname;
    this.age = age;
}

Employee.prototype.print = function(){
    console.log("name : "+this.name);
    console.log("age : "+this.age);
};


module.exports.isExistCollection = function(dbo, colName){
    dbo.collection(colName).drop(function(err, isValid){
        console.log(" [ drop the collection ] ");

        if(err)     return true;
        if(isValid) return false;
    });
}

var cnt = 0;
module.exports.make = function(firstname, lastname, age){
    cnt++;
    result = new Employee(cnt, firstname, lastname, age);
    result.print();
    return result;
}

module.exports.store = function(dbo, dept, employee){
    dbo.collection(dept).insert(employee);
}

module.exports.load = function(dbo, dept, employees = []){
    let cursor = dbo.collection(dept).find();
    cursor.each(function(err,doc){
        if(err){
            console.log(err);
        }
        else{
            if(doc != null){
                console.log(doc);
                employees.push(doc);
            }
        }
    });
}

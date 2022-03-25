const express = require('express')
const app = express()
const porta = process.env.PORT || 3000
const tabela = require('./Trabalho interpolador banco de dados/InfosExcel.json')
var mysql = require('mysql')
const tratamentoTabela = []

var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "",
    database: "concessionaria"
})
con.connect(function(err){
    if(err) throw err;
    
    else{
        tabela.map((item)=>{
            var query = `INSERT INTO veiculos(id,carros,potencia,ano) VALUES('null','${item.carros}','${item.potencia}','${item.ano}')`
            con.query(query,function(err,results){
                console.log(item)
                if(err) throw err;
                console.log(results)
            })
        })
        console.log(" banco conectado")
    }
})
app.listen(porta)
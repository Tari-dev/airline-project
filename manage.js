import express from 'express'
import sql from 'mysql2';
import path from 'path';
import bodyParser from 'body-parser';
const app=express()
const conn=sql.createConnection({
    host:"localhost",
    user:"root",
    password:"1234",
    database:"manage"
})
conn.connect((err)=>{
    if(err){
        console.log("Error occured in connection");
        return;
    }
    console.log("Connected");
})
app.post('/manage',(err,req,res)=>{
    
})
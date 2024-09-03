import express from 'express'
import sql from 'mysql2';
import path from 'path';
import bodyParser from 'body-parser';
const app=express()


const conn=sql.createConnection({
    host:'localhost',
    user:'root',
    password:'1234',
    database:'book_a_flight'
})

conn.connect((err)=>{
    if(err){
        console.log('error')
        return;
    }
    console.log("Connected")
})
app.post('/book_a_flight',(req,res)=>{
    const val=req.body.book_a_flight
    const sql='SELECT * FROM BOOK_A_FLIGHT WHERE FROM_F'
    conn.query(sql,(err,res)=>{
        if(err){
            console.log("Error in Databaes")
        }
        if(res==0){
            console.log("No rows")
        }
        else{
            console.log("Go to next page")
        }
    })
})
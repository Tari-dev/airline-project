import express from 'express'
import sql from 'mysql2';
import path from 'path';
import bodyParser from 'body-parser';
const conn=sql.createConnection({
    host:"localhost",
    user:"root",
    password:"1234",
    database:"flight_status"
});

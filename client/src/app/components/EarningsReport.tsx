"use client";
import {Button} from "@nextui-org/react";
import React, { useState, useEffect } from "react";
import Calendar from 'react-calendar'; 
import 'react-calendar/dist/Calendar.css'; 

async function fetchEarningsData() {
    const res = await fetch("http://localhost:8080/api/getEarningsData");
    return res.json();
}

export default function EarningsReport() {
    const [data, setData] = useState([]);
    const [dateValue, onChange] = useState(new Date()); 

    useEffect(() => {
        async function fetchData() {
            try {
                const responseData = await fetchEarningsData();
                console.log(responseData);
                setData(responseData);
            } catch (error) {
                console.error("Error fetching earnings data:", error);
            }
        }
        fetchData();
    }, []);

  return (
    <div>
        <Button color="primary">
            Button
        </Button>
        <Calendar 
            onChange={onChange} 
            value={dateValue} 
        /> 
    </div>
    );
}

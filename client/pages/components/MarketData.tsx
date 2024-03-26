import React, { useState, useEffect } from "react";

async function fetchMarketData() {
    const res = await fetch("http://localhost:8080/api/getMarketData");
    return res.json();
}

export default function MarketData() {
    const [data, setData] = useState([]);

    useEffect(() => {
        async function fetchData() {
            try {
                const responseData = await fetchMarketData();
                console.log(responseData);
                setData(responseData);
            } catch (error) {
                console.error("Error fetching market data:", error);
            }
        }
        fetchData();
    }, []);

    return (
        <div>
          <div className="market-banner">
            {Object.entries(data).map(([indexName, indexData], index) => (
              <div key={index}>
                <div className="market-label">{indexName}</div>
                <div className="market-value">{indexData.current_price}</div>
                <div className="market-change">{indexData.price_change}</div>
                <div className="market-change-percent">{indexData.price_change_percent}</div>
              </div>
            ))}
          </div>
        </div>
      );
}

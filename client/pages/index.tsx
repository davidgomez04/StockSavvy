import React, {useEffect, useState} from 'react'

function index() {

  // eslint-disable-next-line react-hooks/rules-of-hooks
  const [message, setMessage] = useState("Loading");

  // eslint-disable-next-line react-hooks/rules-of-hooks
  useEffect(() => {
    fetch("http://localhost:8080/api/home")
    .then((response) => response.json())
    .then((data) => {
      setMessage(data.message);
    });
  }, []);

  return (
    <div>
      {message}
    </div>
  )
}

export default index

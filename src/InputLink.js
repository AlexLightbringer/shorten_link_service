import React, { useState } from 'react';
import axios from 'axios'

// create the React component
function InputLink() {
    // create the hook for adding local state to functional components
    const [inputValue, setInputValue] = useState('');
    const [shortLink, setShortLink] = useState('');

    // create the function to handle user input
    const handleInputChange = (e) => {
        setInputValue(e.target.value);
    };

    // send a POST request to the Flask server to shorten the link
    const handleButtonClick = () => {
        axios.post('/shorten', {long_url: inputValue})
            .then(response => {
                //get the shorten link
                setShortLink(response.data.short_url);
                })
            // catch and print an error
            .catch(error => {
                console.error('Error: ', error)
                });
    };

    // copy the link to a user clipboard
    const copyToClipboard = () => {
      navigator.clipboard.writeText(shortLink)
          // send a message to a user
          .then(() => {
              alert('The link copied to your clipboard!')
              })
          // catch and print an error
          .catch(error => {
                console.error('Error: ', error)
                });
    }

    return (
        <div className="container">
            <div className="row">
                <div className="col">
                    <input type='text' className="form-control" placeholder='Enter your link' value={inputValue} onChange={handleInputChange} />
                </div>
                <div className="col">
                    <button className="btn btn-primary" onClick={handleButtonClick}>Create</button>
                </div>
            </div>
            {shortLink && (
                <div className="row mt-3">
                    <div className="col">
                        <input type='text' className="form-control" value={shortLink} readOnly />
                    </div>
                    <div className="col">
                        <button className="btn btn-success" onClick={copyToClipboard}>Copy</button>
                    </div>
                </div>
            )}
        </div>

    );
}

export default InputLink;
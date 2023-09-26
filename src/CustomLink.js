import React, { useState } from 'react';
import axios from 'axios'

// create the React component
function CustomLink() {
    // create the hook for adding local state to functional components
    const [longUrlValue, setLongUrlValue] = useState('');
    const [customShortLinkValue, setCustomShortLinkValue] = useState('');
    const [shortLink, setShortLink] = useState('');
    const [saveClicked, setSaveClicked] = useState(false);

    // create the function to handle user input for original link
    const handleInputLongLink = (e) => {
        setLongUrlValue(e.target.value);
    };

    // create the function to handle user input for original link
    const handleInputCustomShortLink = (e) => {
        setCustomShortLinkValue(e.target.value);
    };

    // receiving the original link from the user
    const handleSend = () => {
        axios.post('/shorten', {long_url: longUrlValue})
            .then(response => {
                setShortLink(response.data.short_url);
            })
            // catch and print an error
            .catch(error => {
                console.error('Error: ', error);
            });
    };

    // receiving a custom short link from the user
    const handleSave = () => {
        axios.post('/custom', { long_url: longUrlValue, short_url: customShortLinkValue })
            .then(response => {
                setShortLink(response.data.custom_link);
                setSaveClicked(true);
            })
            // catch and print an error
            .catch(error => {
                console.error('Error: ', error);
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
                    <input type='text' className="form-control" placeholder='Enter original link' value={longUrlValue} onChange={handleInputLongLink} />
                </div>
                <div className="col">
                    <button className="btn btn-primary" onClick={handleSend}>Send</button>
                </div>
            </div>
            {shortLink && (
                <div>
                    <div className="row mt-3">
                        <div className="col">
                            <input type='text' className="form-control" placeholder='Enter custom short link' value={customShortLinkValue} onChange={handleInputCustomShortLink} />
                        </div>
                        <div className="col">
                            <button className="btn btn-dark" onClick={handleSave}>Save</button>
                        </div>
                    </div>
                    {saveClicked && (
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
            )}
        </div>
    );
}

export default CustomLink;
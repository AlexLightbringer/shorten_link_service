import React from 'react';
import InputLink from "./InputLink";
import CustomLink from "./CustomLink";


function App() {
  return (
    <div className="container">
      <h1 className="blockquote text-center">Shorten My Link</h1>
      <InputLink />
      <h1 className="blockquote text-center">Save My Custom Link</h1>
      <CustomLink/>
    </div>
  );
}

export default App;
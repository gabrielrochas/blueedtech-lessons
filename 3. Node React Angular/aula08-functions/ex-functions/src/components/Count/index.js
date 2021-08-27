import { useState } from 'react';

export default function Count() {
  const [count, setCount] = useState(1);
  
  return (
    <>
      <p>{ count }</p>
      <button onClick={() => setCount(count + 1)} >Add 1</button>
    </>
  );
}

import React from 'react';

export default function Spinner() {
  return (
    <div style={{ textAlign: 'center', marginTop: 20 }}>
      <div style={{ border: '4px solid #f3f3f3', borderTop: '4px solid #3498db', borderRadius: '50%', width: 40, height: 40, animation: 'spin 1s linear infinite' }} />
      <style>
        {`
          @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
          }
        `}
      </style>
    </div>
  );
}
import React from 'react'

export default function Job_Openings_Page(props) {
  return (
    <div>
      
      {
        props.backendResponse && (
            <div>
                
              <p>{props.backendResponse}</p>
    
    
            </div>
          )
      }
    </div>
  )
}

import React from 'react'

export default function Alert(props) {

    const capitalizeFirstLetter = (string)=>{
        if (string === 'danger'){
            return "Error"
        }
        return string.charAt(0).toUpperCase() + string.slice(1);
    }
  return (
    <div>
    {props.alert &&  <div className={`alert fixed-top alert-${props.alert.type}` }role="alert">
    <b>{capitalizeFirstLetter(props.alert.type)}</b> : {props.alert.message}
</div>
     }    
    </div>
  )
}
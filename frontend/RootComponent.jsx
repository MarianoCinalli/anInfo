import React from 'react'

export default class RootComponent extends React.Component {

    ajaxCall(entrypoint, params, onSuccess = null, onError = null) {
        if (params){
            var body = JSON.stringify(params)
            var method = 'POST'
        }
        else {
            var method = 'GET'
        }
        fetch(entrypoint, {
            method: method,
            body: body,
            credentials: 'same-origin'
        })
        .then(r => r.json())
        .then(r => {
            if (onSuccess) onSuccess(r, params)
            else console.log(r)
        })
        .catch(err => {
            if (onError) onError()
            else console.log(err)
        })
    }

    objIsEmpty(obj){
        var isEmpty = (Object.keys(obj).length === 0 && obj.constructor === Object)
        return isEmpty
    }


    copy(obj){
        var copy = JSON.parse(JSON.stringify(obj))
        return copy
    }

    capitalizeFirstLetter(string) {
        return string.charAt(0).toUpperCase() + string.slice(1);
    }

}

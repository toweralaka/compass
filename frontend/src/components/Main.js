import React from "react"
import logo from '../images/gift-habeshaw-eR0dgeG1wqY-unsplash.jpg';



export default function Main() {
    return(
        <div className="row my-5">
            <div className="col-md-7 rounded-5 formImgWrap">
            <img className="rounded-3 formImg" src={logo} alt="Logo"/>
            </div>
            <div className="col-md-5 h-100 p-3 my-5 rounded-3 border homeForm">
                <form className="h-full w-9/10 my-4 mx-auto">
                    <label>
                    Username
                        <input/>
                    </label>
                </form>
            </div>

        </div>
    )
}
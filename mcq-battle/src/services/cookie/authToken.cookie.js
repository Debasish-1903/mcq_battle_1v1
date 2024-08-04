import { Cookies, Cookies } from "react-cookie";
const cookies= new Cookies();

const SetAccessToken=(accessToken)=>{

    return cookies.set("access_token",accessToken,{
        path :"/",
        expires :new Date(new Date().getTime()+ 28*60*1000),

    });

}

const SetRefreshToken = (refreshToken) => {
  return cookies.set("refresh_token", refreshToken, {
    path: "/",
    expires: new Date(new Date().getTime() + 1000 * 60 * 1000),
  });
};

const GetAccessToken = () => {
  return cookies.get("access_token", {
    path: "/" });
};

const GetRefreshToken = () => {
  return cookies.get("refresh_token", {
    path: "/",
  });
};

const ClearAll=()=>{
    cookies.remove("access_token",{path:"/"});
    cookies.remove("refresh_token",{path:"/"});
}


export default {

  SetAccessToken,
  SetRefreshToken,
  GetAccessToken,
  GetRefreshToken,
  ClearAll
}
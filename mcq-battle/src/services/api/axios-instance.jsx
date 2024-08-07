import axios from "axios";
import authTokenCookie from "../cookie/authToken.cookie";
const BASE_URL = import.meta.env.VITE_BASE_API_URL;


const axiosInstance=axios.create({ baseURL: `${BASE_URL}`});

axios.interceptors.request.use(
  (config)=>{
    // Do something before request is sent
   // config.url=BASE_URL +config.url

    const token = authTokenCookie.GetAccessToken();
     
    if(token){
        config.headers["Authorization"]=`Bearer ${token}`
    }


    return config;
  },
  (error)=>{
    // handle request error here 
    return Promise.reject(error);
  }
);

export default axiosInstance;
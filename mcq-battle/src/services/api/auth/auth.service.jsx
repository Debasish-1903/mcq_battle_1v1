import axiosInstance from "../axios-instance"


export const Signup= async(data)=>{

    return await axiosInstances.post(`/register`,data);

}

export const Login =async(data)=>{
    return await axiosInstance.post(`/login`,data);
}

export const Protected = async(data)=>{
    return await axiosInstance.get(`/protected`);
}
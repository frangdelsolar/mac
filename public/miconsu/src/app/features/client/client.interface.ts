// import { ClientPlan } from "./client-plan.interface";
// import { ClientType } from "./client-type.interface";
// import { User } from "./user.interface";


export interface Client {
    id: number;
    name: string
    administrator?: any;
    client_plan?: any;
    client_type?: any;
}
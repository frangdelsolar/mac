import { ClientPlan } from "@features/client-plan/client-plan.interface";
import { ClientType } from "@features/client-type/client-type.interface";
import { User } from "@features/user/user.interface";


export interface Client {
    id: number;
    name: string
    administrator?: User;
    client_plan?: ClientPlan;
    client_type?: ClientType;
}
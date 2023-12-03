// import ActivityStore from "./activityStore";
import {createContext, useContext} from "react";
import CommonStore from "./commonStore";
import UserDataStore from "./userDataStore";
// import UserStore from "./userStore";
// import ModalStore from "./modalStore";
// import ProfileStore from "./profileStore";
// import CommentStore from "./commentStore";

interface Store {
    // activityStore: ActivityStore;
    commonStore: CommonStore;
    userDataStore: UserDataStore;
    // modalStore: ModalStore;
    // profileStore: ProfileStore;
    // commentStore: CommentStore;
}

export const store: Store = {
    userDataStore: new UserDataStore(),
    commonStore: new CommonStore(),
    // userStore: new UserStore(),
    // modalStore: new ModalStore(),
    // profileStore: new ProfileStore(),
    // commentStore: new CommentStore()
}

export const StoreContext = createContext(store);

export function useStore() {
    return useContext(StoreContext);
}
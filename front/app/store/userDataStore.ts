import { makeAutoObservable, reaction, runInAction } from "mobx";
import { IUserData } from "../models/profile";
import agent from "../api/agent";

export default class UserDataStore {
  constructor() {
    makeAutoObservable(this);
  }
  postUserData = async (userData: IUserData) => {
    try {
      const responce = await agent.UserData.create(userData);
      return responce;
      //   const newActivity = new Activity(activity);
      //   newActivity.hostUsername = user!.username;
      //   newActivity.attendees = [profile];
      //   this.setActivity(newActivity);
      //   runInAction(() => (this.selectedActivity = newActivity));
    } catch (error) {
      console.log(error);
    }
  };
}

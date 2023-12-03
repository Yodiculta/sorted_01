export interface IUserData {
  id?: string;
  name: string;
  areaOfDevelopment: string;
  experienceDescription: string;
  // username?: string;
}
export class UserDataClass {
  id?: string = undefined;
  name: string = "";
  areaOfDevelopment: string = "";
  description: string = "";
  experienceDescription: string = "";
  constructor(data?: IUserData) {
    if (data) {
      this.id = data?.id;
      this.name = data.name;
      this.areaOfDevelopment = data.areaOfDevelopment;
      this.experienceDescription = data.experienceDescription;
    }
  }
}

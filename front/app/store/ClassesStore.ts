export type ClassItemType = {
    id: number;
    title: string;
  }
  
  export class ClassesStore {
    items: ClassItemType[] = [];
  }
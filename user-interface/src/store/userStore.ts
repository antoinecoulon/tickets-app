import { create } from "zustand";
import { persist } from "zustand/middleware";

type Role = "client" | "agent" | "admin" | null;

interface UserStore {
  token: string | null;
  role: Role;
  username: string | null;
  setUser: (token: string, role: Role, username: string) => void;
  logout: () => void;
}

export const useUserStore = create<UserStore>()(
  persist(
    (set) => ({
      token: null,
      role: null,
      username: null,
      setUser: (token, role, username) => set({ token, role, username }),
      logout: () => set({ token: null, role: null, username: null }),
    }),
    {
      name: "user-storage",
    }
  )
);

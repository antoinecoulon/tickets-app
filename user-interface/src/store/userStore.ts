import { createStore, useStore } from "zustand";
import { createJSONStorage, persist } from "zustand/middleware";

type Role = "client" | "agent" | "admin" | null;

interface UserStore {
  token: string | null;
  role: Role;
  username: string | null;
  isHydrated: boolean
  setUser: (token: string, role: Role, username: string) => void;
  logout: () => void;
  setHydrated: () => void
}

export const userStore = createStore<UserStore>()(
  persist(
    (set) => ({
      token: null,
      role: null,
      username: null,
      isHydrated: false,
      setUser: (token, role, username) => set({ token, role, username }),
      logout: () => set({ token: null, role: null, username: null }),
      setHydrated: () => set({ isHydrated: true })
    }),
    {
      name: "user-storage",
      storage: createJSONStorage(() => localStorage),
    }
  )
);

export const useUserStore = <T>(selector: (state: UserStore) => T) =>
  useStore(userStore, selector)
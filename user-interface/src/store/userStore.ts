import { createStore, useStore } from "zustand";
import { createJSONStorage, persist } from "zustand/middleware";

type Role = "client" | "agent" | "admin" | null;

interface UserStore {
  token: string | null;
  refreshToken: string | null;
  role: Role;
  username: string | null;
  isHydrated: boolean;
  setUser: (
    token: string,
    refreshToken: string,
    role: Role,
    username: string
  ) => void;
  logout: () => void;
  setHydrated: () => void;
}

export const userStore = createStore<UserStore>()(
  persist(
    (set) => ({
      token: null,
      refreshToken: null,
      role: null,
      username: null,
      isHydrated: false,
      setUser: (token, refreshToken, role, username) =>
        set({ token, refreshToken, role, username }),
      logout: () => {
        set({ token: null, role: null, username: null });
        localStorage.removeItem("user-storage");
        sessionStorage.clear();
      },
      setHydrated: () => set({ isHydrated: true }),
    }),
    {
      name: "user-storage",
      storage: createJSONStorage(() => localStorage),
    }
  )
);

export const useUserStore = <T>(selector: (state: UserStore) => T) =>
  useStore(userStore, selector);

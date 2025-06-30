"use client";

import Header from "@/components/Header";
import HydrationGate from "@/components/HydrationGate";
import Sidebar from "@/components/Sidebar";
import { useUserStore } from "@/store/userStore";
import { useRouter } from "next/navigation";
import React, { useEffect } from "react";

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const router = useRouter()
  const token = useUserStore((state) => state.token)

  useEffect(() => {    
    if (!token) {
      router.push("/login")
    }
  }, [token])
  
  return (
    <HydrationGate>
      <div className="flex h-screen bg-gray-100 text-gray-900">
        <Sidebar />
        <div className="flex flex-col flex-1">
          <Header />
          <main className="flex-1 overflow-y-auto p-6">{children}</main>
        </div>
      </div>
    </HydrationGate>
  );
}

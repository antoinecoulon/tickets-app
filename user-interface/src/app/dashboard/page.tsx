"use client";

import { useRouter } from "next/navigation";
import { useEffect } from "react";

export default function DashboardHome() {
  const router = useRouter();

  useEffect(() => {
    router.replace("/dashboard/tickets");
  }, []);

  return null;
}

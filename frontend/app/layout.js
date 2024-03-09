'use client'

import { Inter } from "next/font/google";
import "./globals.css";
import Navbar from "./components/navigation/navbar";

const inter = Inter({ subsets: ["latin"] });

// export const metadata = {
//   title: "AI Art on a Cob",
//   description: "A simple app for generating AI art in bulk",
// };

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <Navbar />
        <div className="m-10">
          {children}
        </div>
      </body>
    </html>
  );
}

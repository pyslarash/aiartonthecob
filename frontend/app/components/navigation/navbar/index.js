'use client'

import React from "react";
import Link from "next/link";
import Image from "next/image";
import Logo from "./logo.png"
import styles from "./styles.module.css";
import { usePathname } from 'next/navigation'

const Navbar = () => {
  const pathname = usePathname()

  return (
    <>
      <div className="w-full h-20 bg-black sticky top-0 border-slate-400 border-b-2">
        <div className="container mx-auto px-4 h-full">
          <div className="flex justify-between items-center h-full">
            <Link href="/">
                <div className="flex items-center">
                    <div className="rounded-full overflow-hidden mr-2">
                        <Image src={Logo} alt="Logo" width={50} height={50} />
                    </div>
                    <span className="text-white ml-2">AI Art on a Cob</span>
                </div>
            </Link>
            <ul className="hidden md:flex gap-x-6 text-white">
              <li>
                <Link href="/dalle">
                  <p className={pathname === "/dalle" ? `${styles.nav} ${styles.active}` : styles.nav}>Dall-E</p>
                </Link>
              </li>
              <li>
                <Link href="/stability">
                  <p className={pathname === "/stability" ? `${styles.nav} ${styles.active}` : styles.nav}>Stability AI</p>
                </Link>
              </li>
              <li>
                <Link href="/description">
                  <p className={pathname === "/description" ? `${styles.nav} ${styles.active}` : styles.nav}>Description</p>
                </Link>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </>
  );
};

export default Navbar;
"use client";
import React from "react";
import {Navbar, NavbarBrand, NavbarContent, NavbarItem, Link, Button} from "@nextui-org/react";

const NavBar = () => {
    return (
        <Navbar>
            <NavbarBrand>
                {/* <AcmeLogo /> */}
                <p className="font-bold text-inherit">StockSavvy</p>
            </NavbarBrand>
            <NavbarContent className="hidden sm:flex gap-4" justify="center">
                <NavbarItem>
                <Link color="foreground" href="#">
                    Portfolio
                </Link>
                </NavbarItem>
                <NavbarItem isActive>
                <Link href="#" aria-current="page">
                    News
                </Link>
                </NavbarItem>
                <NavbarItem>
                <Link color="foreground" href="/earnings">
                    Earnings
                </Link>
                </NavbarItem>
            </NavbarContent>
            <NavbarContent justify="end">
                <NavbarItem className="hidden lg:flex">
                <Link href="#">Login</Link>
                </NavbarItem>
                <NavbarItem>
                <Button as={Link} color="primary" href="#" variant="flat">
                    Sign Up
                </Button>
                </NavbarItem>
            </NavbarContent>
        </Navbar>
    );
};

export default NavBar;


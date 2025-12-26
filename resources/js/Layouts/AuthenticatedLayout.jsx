import { useState } from 'react';
import ApplicationLogo from '@/Components/ApplicationLogo';
import Dropdown from '@/Components/Dropdown';
import NavLink from '@/Components/NavLink';
import { Link, usePage } from '@inertiajs/react';
import Icon from '@/Components/Icon';

export default function AuthenticatedLayout({ header, children }) {
    const { auth } = usePage().props;
    const { user, roles } = auth;
    console.log('User roles:', roles);
    const [sidebarCollapsed, setSidebarCollapsed] = useState(false);
    const [settingsOpen, setSettingsOpen] = useState(false);

    return (
        <div className="flex h-screen bg-gray-100">
            {/* Sidebar */}
            <aside className={`bg-gray-800 text-white flex-shrink-0 transition-all duration-300 ${sidebarCollapsed ? 'w-20' : 'w-64'}`}>
                <div className="flex items-center justify-center h-16 bg-gray-900">
                    <Link href="/">
                        <ApplicationLogo className="block h-9 w-auto fill-current text-white" />
                    </Link>
                </div>
                <nav className="mt-5">
                    <NavLink href={route('dashboard')} active={route().current('dashboard')} icon="dashboard">
                        {!sidebarCollapsed && 'Dashboard'}
                    </NavLink>
                    {roles.includes('admin') && (
                        <div>
                            <button onClick={() => setSettingsOpen(!settingsOpen)} className="w-full flex items-center justify-between px-4 py-2 text-gray-300 hover:bg-gray-700 hover:text-white">
                                <div className="flex items-center">
                                    <Icon name="settings" className="w-6 h-6" />
                                    {!sidebarCollapsed && <span className="ml-2">Settings</span>}
                                </div>
                                {!sidebarCollapsed && <Icon name={settingsOpen ? 'chevron-down' : 'chevron-right'} className="w-4 h-4" />}
                            </button>
                            {settingsOpen && !sidebarCollapsed && (
                                <div className="pl-8 py-2">
                                    <Link href={route('users.index')} className={`flex items-center text-gray-300 hover:text-white ${route().current('users.index') ? 'text-white' : ''}`}>
                                        <Icon name="users" className="w-5 h-5" />
                                        <span className="ml-2">User Management</span>
                                    </Link>
                                </div>
                            )}
                        </div>
                    )}
                </nav>
                <div className="absolute bottom-0 w-full">
                    <button onClick={() => setSidebarCollapsed(!sidebarCollapsed)} className="w-full flex items-center justify-center py-4 text-gray-300 hover:bg-gray-700 hover:text-white">
                        <Icon name={sidebarCollapsed ? 'chevron-right' : 'chevron-left'} className="w-6 h-6" />
                    </button>
                </div>
            </aside>

            <div className="flex flex-col flex-1 overflow-y-auto">
                {/* Top bar */}
                <header className="bg-white shadow">
                    <div className="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8 flex justify-between items-center">
                        <div>{header}</div>
                        <div className="hidden sm:ms-6 sm:flex sm:items-center">
                            <div className="relative ms-3">
                                <Dropdown>
                                    <Dropdown.Trigger>
                                        <span className="inline-flex rounded-md">
                                            <button
                                                type="button"
                                                className="inline-flex items-center rounded-md border border-transparent bg-white px-3 py-2 text-sm font-medium leading-4 text-gray-500 transition duration-150 ease-in-out hover:text-gray-700 focus:outline-none"
                                            >
                                                {user.name}

                                                <svg
                                                    className="-me-0.5 ms-2 h-4 w-4"
                                                    xmlns="http://www.w3.org/2000/svg"
                                                    viewBox="0 0 20 20"
                                                    fill="currentColor"
                                                >
                                                    <path
                                                        fillRule="evenodd"
                                                        d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
                                                        clipRule="evenodd"
                                                    />
                                                </svg>
                                            </button>
                                        </span>
                                    </Dropdown.Trigger>

                                    <Dropdown.Content>
                                        <Dropdown.Link href={route('profile.edit')}>
                                            Profile
                                        </Dropdown.Link>
                                        <Dropdown.Link href={route('logout')} method="post" as="button">
                                            Log Out
                                        </Dropdown.Link>
                                    </Dropdown.Content>
                                </Dropdown>
                            </div>
                        </div>
                    </div>
                </header>

                {/* Main content */}
                <main className="p-6">{children}</main>
            </div>
        </div>
    );
}

import { Link } from '@inertiajs/react';
import Icon from './Icon';

export default function NavLink({ active = false, className = '', icon, children, ...props }) {
    return (
        <Link
            {...props}
            className={
                'flex items-center w-full px-4 py-2 text-left text-sm font-medium leading-5 transition duration-150 ease-in-out focus:outline-none ' +
                (active
                    ? 'bg-gray-900 text-white'
                    : 'text-gray-300 hover:bg-gray-700 hover:text-white') +
                className
            }
        >
            {icon && <Icon name={icon} className="w-6 h-6 mr-2" />}
            {children}
        </Link>
    );
}

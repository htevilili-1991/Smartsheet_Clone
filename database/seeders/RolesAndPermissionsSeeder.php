<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use Spatie\Permission\Models\Role;
use Spatie\Permission\Models\Permission;
use App\Models\User;

class RolesAndPermissionsSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        // Reset cached roles and permissions
        app()[\Spatie\Permission\PermissionRegistrar::class]->forgetCachedPermissions();

        // create permissions
        $permissions = [
            'create_project',
            'edit_project',
            'delete_project',
            'view_project',
            'create_task',
            'edit_task',
            'delete_task',
            'assign_task',
            'view_all_tasks',
        ];

        foreach ($permissions as $permission) {
            Permission::create(['name' => $permission]);
        }

        // create roles and assign existing permissions
        $adminRole = Role::create(['name' => 'admin']);
        $adminRole->givePermissionTo(Permission::all());

        $projectManagerRole = Role::create(['name' => 'project_manager']);
        $projectManagerRole->givePermissionTo([
            'create_project',
            'edit_project',
            'delete_project',
            'view_project',
            'create_task',
            'edit_task',
            'delete_task',
            'assign_task',
            'view_all_tasks',
        ]);

        $teamMemberRole = Role::create(['name' => 'team_member']);
        $teamMemberRole->givePermissionTo([
            'view_project',
            'edit_task',
            'view_all_tasks',
        ]);

        $viewerRole = Role::create(['name' => 'viewer']);
        $viewerRole->givePermissionTo([
            'view_project',
            'view_all_tasks',
        ]);

        // assign admin role to the first user
        $user = User::find(1);
        if ($user) {
            $user->assignRole($adminRole);
        }
    }
}
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    """generate the launch description"""
    # Declare launch argument for number of machines
    num_machines_arg = DeclareLaunchArgument(
        'num_machines',
        default_value='3',
        description='Number of blimps to launch (integer)'
    )

    # Initialize LaunchDescription
    ld = LaunchDescription()

    # Add the launch argument
    ld.add_action(num_machines_arg)

    # Get the number of machines from launch argument
    num_machines = LaunchConfiguration('num_machines')

    # Loop to create nodes for each blimp
    for robot_id in range(1, int(num_machines) + 1):
        node = Node(
            package='blimp_nmpc_formation_control',
            executable='blimp_nmpc_formation_controller',
            name=f'blimp_nmpc_formation_controller_{robot_id}',
            namespace=f'machine_{robot_id}',
            parameters=[{
                'robotID': robot_id,
                'numRobots': int(num_machines),
                'PREFIX': '/machine_',
                # 'POSETOPIC': 'throttledUAVPose',
                'use_sim_time': False,
                'start_type_description_service': False
            }],
            output='screen'
        )
        ld.add_action(node)

    return ld

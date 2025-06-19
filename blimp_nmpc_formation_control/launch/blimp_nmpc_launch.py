from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration

def launch_nodes(context, num_machines):
    # Evaluate the num_machines launch argument
    num = int(context.perform_substitution(num_machines))
    
    # Create a list to hold node actions
    nodes = []
    
    # Loop to create nodes for each blimp
    for robot_id in range(1, num + 1):
        node = Node(
            package='blimp_nmpc_formation_control',
            executable='blimp_nmpc_formation_controller',
            name=f'blimp_nmpc_formation_controller_{robot_id}',
            namespace=f'machine_{robot_id}',
            parameters=[{
                'robotID': robot_id,
                'numRobots': num,
                'PREFIX': '/machine_',
                # 'POSETOPIC': 'throttledUAVPose',
                'use_sim_time': False,
                'start_type_description_service': False
            }],
            output='screen'
        )
        nodes.append(node)
    
    return nodes

def generate_launch_description():
    # Declare launch argument for number of machines
    num_machines_arg = DeclareLaunchArgument(
        'num_machines',
        default_value='3',
        description='Number of blimps to launch (integer)'
    )
    
    # Get the number of machines launch configuration
    num_machines = LaunchConfiguration('num_machines')
    
    # Create LaunchDescription
    ld = LaunchDescription([
        num_machines_arg,
        OpaqueFunction(function=launch_nodes, args=[num_machines])
    ])
    
    return ld
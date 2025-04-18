import launch
import launch_ros.actions

def generate_launch_description():
    livox_repub_node = launch_ros.actions.Node(
        package='nav2_bringup',
        executable='livox_repub',
        name='livox_repub',
        output='screen',
        remappings=[('/livox_pcl0', '/livox_pcl0')]
    )

    return launch.LaunchDescription([livox_repub_node])

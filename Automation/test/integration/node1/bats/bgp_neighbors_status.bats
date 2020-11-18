#!/usr/bin/env bats

@test "Check if 10.1.1.2 bgp neighbor is UP" {
	run sudo net show bgp neighbor 10.1.1.2
	[[ "${output}" =~ "BGP state = Established" ]]
}

@test "Check if 10.1.2.2 bgp neighbor is UP" {
        run sudo net show bgp neighbor 10.1.2.2
        [[ "${output}" =~ "BGP state = Established" ]]
}

package main

import "testing"

func Test_smash(t *testing.T) {
	type args struct {
		words []string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		// TODO: Add test cases.
		{
			name: "simple smashing",
			args: args{
				words: []string{""},
			},
			want: "",
		},
		{
			name: "hello",
			args: args{
				words: []string{"hello"},
			},
			want: "hello",
		},
		{
			name: "hello world",
			args: args{
				words: []string{"hello", "world"},
			},
			want: "hello world",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := smash(tt.args.words); got != tt.want {
				t.Errorf("smash() = %v, want %v", got, tt.want)
			}
		})
	}
}
